const Joi = require('joi');

/**
 * This is object with schemas which can be used to verify if received requests are valid.
 */
const Validation = {

  addingTaskSchema: {
    options: { allowUnknownBody: false },
    body: {
      description: Joi.string().min(1).required(),
      position: Joi.number().required()
    }
  },

  updateStatusOfTaskSchema: {
    options: { allowUnknownBody: false },
    body: {
      completed: Joi.number().min(0).max(1).required()
    }
  },

  changePositionOfTaskSchema: {
    options: { allowUnknownBody: false },
    body: {
      newPosition: Joi.number().required(),
      previousPosition: Joi.number().required()
    }
  }
}

module.exports = Validation;
