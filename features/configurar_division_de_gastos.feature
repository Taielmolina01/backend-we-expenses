Feature: Configurar división de gastos
  Como usuario perteneciente a un grupo
  Quiero configurar la forma en que se dividen los gastos
  Para asegurar que cada miembro pague según sus ingresos

  Scenario: Configurar división por porcentaje
    Given soy administrador del grupo
    When configuro la división de gastos por porcentaje para cada miembro
    Then se aplica correctamente a los gastos futuros del grupo

  Scenario: Configurar división por cantidad fija
    Given soy administrador del grupo
    When configuro la división de gastos por cantidad fija para cada miembro
    Then se aplica correctamente a los gastos futuros del grupo

  Scenario: Configurar división sin ser administrador
    Given no soy administrador del grupo
    When intento cambiar la forma de dividir los gastos
    Then no puedo hacerlo y me avisa que no tengo permisos.