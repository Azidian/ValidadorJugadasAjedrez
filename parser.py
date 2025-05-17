import re
from typing import List
from partida import Partida
from turno import Turno
from jugada import Jugada

class ParserSAN: # Permite analizar una partida completa en formato de texto y convertirla a objetos estructurados.
    """
    Analizador sintáctico para partidas de ajedrez en notación algebraica estándar (SAN).
    Convierte texto en formato SAN a objetos estructurados (Partida, Turno, Jugada).
    """

    # Expresiones regulares para validación de movimientos
    RE_ENROQUE = re.compile(r'^(O-O|O-O-O)(\+|#)?$')
    RE_PIEZA = re.compile(r'^([KQRBN])([a-h]?[1-8]?)(x?)([a-h][1-8])(=[QRBN])?(\+|#)?$')
    RE_PEON_AVANCE = re.compile(r'^([a-h])([1-8])(=[QRBN])?(\+|#)?$')
    RE_PEON_CAPTURA = re.compile(r'^([a-h])(x)([a-h])([1-8])(=[QRBN])?(\+|#)?$')
    RE_TURNO = re.compile(r'^(\d+)\.\.?$')  # acepta "1." o "1.."
    RE_RESULTADO = re.compile(r'^(1-0|0-1|1/2-1/2|\*)$')

    def __init__(self, texto_partida: str):
        self.texto = texto_partida
        self.tokens = texto_partida.split()
        self.pos = 0
        self.turno_esperado = 1
        
    def obtenerElementos(self):
        return self.texto

    def parse(self) -> Partida:        
        turnos: List[Turno] = []
        try:
            while self.pos < len(self.tokens):
                turno = self._parse_turno()
                turnos.append(turno)
                self.turno_esperado += 1
            return Partida(turnos)
        except ValueError as e:
            raise ValueError(f"Error en posición {self.pos}: {str(e)}")

    def _parse_turno(self) -> Turno:
        token_num = self._next_token()
        if not self.RE_TURNO.match(token_num):
            raise ValueError(f"Formato de turno inválido: '{token_num}'")
        
        numero = int(token_num[:-1])
        if numero != self.turno_esperado:
            raise ValueError(f"Turno fuera de serie: esperado {self.turno_esperado}, obtenido {numero}")

        # Parsear jugada blanca
        jug_blanca = self._parse_jugada()
        
        # Parsear jugada negra
        jug_negra = None
        if self.pos < len(self.tokens) and not self.RE_TURNO.match(self.tokens[self.pos]):
            jug_negra = self._parse_jugada()

        return Turno(numero, jug_blanca, jug_negra)

    def _parse_jugada(self) -> Jugada:
        token = self._next_token()
        
        if self._es_enroque(token):
            return Jugada(token)
        elif self._es_movimiento_pieza(token):
            return Jugada(token)
        elif self._es_mov_peon(token):
            return Jugada(token)
        
        raise ValueError(f"Movimiento inválido: '{token}'")

    def _es_enroque(self, token: str) -> bool:
        return bool(self.RE_ENROQUE.match(token))

    def _es_movimiento_pieza(self, token: str) -> bool:
        return bool(self.RE_PIEZA.match(token))

    def _es_mov_peon(self, token: str) -> bool:
        return (bool(self.RE_PEON_AVANCE.match(token)) or 
                bool(self.RE_PEON_CAPTURA.match(token)))

    def _next_token(self) -> str:
        if self.pos >= len(self.tokens):
            raise ValueError("Fin no esperado de la entrada")
        token = self.tokens[self.pos]
        self.pos += 1
        return token
