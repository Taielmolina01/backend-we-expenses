Feature: Liquidar deudas
  Como usuario registrado de la aplicación
  Quiero liquidar mis deudas de un grupo/evento
  Para que quede registrado que ya pagué lo que debía

  Scenario: Liquidar deudas sin ser parte de un evento/grupo
    Given no soy parte de un evento/grupo
    When liquido mis deudas del evento/grupo
    Then no liquido mis deudas

  Scenario: Liquidar deudas siendo el único participante
    Given soy parte de un evento/grupo en el que soy el único participante
    When liquido mis deudas del evento/grupo
    Then mi saldo actual sigue siendo el previo

  Scenario: Liquidar deudas siendo parte de un evento/grupo con más participantes
    Given soy parte de un evento/grupo en el que hay más de un participante
    When liquido mis deudas del evento/grupo
    Then mi saldo actual es $0