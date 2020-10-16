const express = require('express');
const app = express();
const morgan = require('morgan');
const cookieParser = require('cookie-parser');

const db = require('../backend/db/models');
const { Exercise, Muscle } = db;

const pagesRouter = require('./src/routes/pages');
const musclesRouter = require('./src/routes/api/muscles');
const exercisesRouter = require('./src/routes/api/exercises');
const programsRouter = require('./src/routes/api/programs');
const workoutsRouter = require('./src/routes/api/workouts');

app.set('view engine', 'pug');

app.use(morgan('dev'));
app.use(cookieParser());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use((req, res, next) => {
  res.setTimeout(1000);
  req.setTimeout(1000);

  next();
});

app.use(async (req, res, next) => {
  const muscles = await Muscle.findAll();
  const exercises = await Exercise.findAll();
  req.muscles = muscles;
  req.exercises = exercises;
  next();
});
app.use('/public', express.static('public'));

app.use('/', pagesRouter);
app.use('/muscles', musclesRouter);
app.use('/exercises', exercisesRouter);
app.use('/programs', programsRouter);
app.use('/workouts', workoutsRouter);

app.use((req, res, next) => {
  const err = new Error('Error occurred...');
  err.status = 404;
  next(err);
});

app.use((err, req, res, next) => {
  console.log(err);
});

app.use((err, req, res, next) => {
  if (err.status === 404) {
    res.status(404);
    res.render('errors/page-not-found', {
      title: err.status,
    });
  } else {
  }
  res.status(err.status || 500);
  res.render('errors/generic', {
    title: err.status || 500,
  });
});

module.exports = app;