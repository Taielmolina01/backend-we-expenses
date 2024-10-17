Feature: Cambiar nombre del grupo
  Como usuario perteneciente a un grupo
  Quiero cambiar el nombre del grupo
  Para poder actualizarlo

  Scenario: Cambiar nombre siendo administrador
    Given soy administrador del grupo
    When cambio el nombre del grupo y lo confirmo
    Then el nombre del grupo se actualiza correctamente

  Scenario: Cambiar nombre sin ser administrador
    Given no soy administrador del grupo
    When intento cambiar el nombre del grupo
    Then no puedo cambiarlo y me avisa que no tengo permisos.