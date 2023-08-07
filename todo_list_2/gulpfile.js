const gulp = require('gulp'),
      nodemon = require('gulp-nodemon'),  
      sass = require('gulp-ruby-sass'),
      autoprefixer = require('gulp-autoprefixer'),
      livereload = require('gulp-livereload');

gulp.task('styles', function() {  
  return sass('frontend/style/*.scss', { style: 'expanded' })
    .pipe(autoprefixer('last 2 version'))
    .pipe(gulp.dest('frontend/style'))
    .pipe(livereload());
});
        
gulp.task('scripts', function() {  
  return gulp.src('frontend/js/*.js')
    .pipe(livereload());
});

gulp.task('html',function(){  
    return gulp.src('frontend/*.html')
    .pipe(livereload());
});

gulp.task('watch', function() {  
    livereload.listen();
    gulp.watch('frontend/style/*.scss', ['styles']);
    gulp.watch('frontend/js/*.js', ['scripts']);
    gulp.watch('frontend/*.html', ['html']);
});

gulp.task('server',function(){  
    nodemon({
        'script': 'backend/server.js'
    });
});

gulp.task('start', ['server','watch']);  
