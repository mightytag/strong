'use strict';
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('Exercise_Equipments', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER,
      },
      exerciseId: {
        type: Sequelize.INTEGER,
        references: { model: 'Exercises' },
      },
      equipmentId: {
        type: Sequelize.INTEGER,
        references: { model: 'Equipment' },
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE,
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE,
      },
    });
  },
  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('Exercise_Equipments');
  },
};
