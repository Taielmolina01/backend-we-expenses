Feature: Actualizar grupo
  Como usuario perteneciente a un grupo
  Quiero cambiar el nombre o la foto del grupo
  Para poder actualizarlo

  Scenario: Cambiar foto siendo administrador
    Given soy administrador del grupo
    When subo una nueva foto para el grupo
    Then la foto del grupo se actualiza correctamente

  Scenario: Cambiar foto sin ser administrador
    Given no soy administrador del grupo
    When intento cambiar la foto del grupo
    Then no puedo cambiarla y me avisa que no tengo permisos.

  Scenario: Cambiar nombre siendo administrador
    Given soy administrador del grupo
    When cambio el nombre del grupo y lo confirmo
    Then el nombre del grupo se actualiza correctamente

  Scenario: Cambiar nombre sin ser administrador
    Given no soy administrador del grupo
    When intento cambiar el nombre del grupo
    Then no puedo cambiarlo y me avisa que no tengo permisos.