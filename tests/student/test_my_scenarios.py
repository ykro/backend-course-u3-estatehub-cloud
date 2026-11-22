"""Tus tests propios (al menos 2).

Un buen test propio pasa con tu código y falla si siembras a propósito un error plausible
que los tests de la plantilla no atrapan: por ejemplo, un fallo que sigue contando a los 900
segundos exactos o un Retry-After truncado. Compruébalo: mete el error, corre
`uv run pytest tests/student -v`, confirma que tu test falla y deshaz el cambio con
`git restore`. Reescribir un test de la plantilla no atrapa nada nuevo.
Usa los fixtures de tests/conftest.py: client, clock, login y, para peticiones simultáneas con
hilos, file_client. No agregues conftest.py aquí.
"""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient


def test_my_scenario_1(client: TestClient) -> None:
    _ = client
    pytest.fail("Escribe un escenario que detecte un error de autorización o de autenticación.")


def test_my_scenario_2(client: TestClient) -> None:
    _ = client
    pytest.fail("Escribe un escenario de borde del reto (ventana, normalización o reinicio).")
