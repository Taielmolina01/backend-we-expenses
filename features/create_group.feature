Feature: Creación de grupos
  Como usuario registrado de la aplicación
  Quiero poder crear grupos para invitar a mis amigos de salida recurrentes
  Para manejar los gastos del grupo

  Scenario: Crear un grupo con un ID existente
    Given estoy registrado en la aplicación
    When creo un grupo con un id de grupo ya existente
    Then no se crea el grupo

  Scenario: Crear un grupo con un ID no existente
    Given estoy registrado en la aplicación
    When creo un grupo con un id de grupo no existente
    Then se crea el grupo

  Scenario: Invitar amigos no registrados
    Given estoy registrado en la aplicación
    When invito a mi grupo a mis amigos por nombres de usuario no registrados
    Then no los invito y me avisa diciendo “no existe ese usuario”

  Scenario: Invitar amigos registrados
    Given estoy registrado en la aplicación
    When invito a mi grupo a mis amigos por nombres de usuarios registrados
    Then se los envía la invitación