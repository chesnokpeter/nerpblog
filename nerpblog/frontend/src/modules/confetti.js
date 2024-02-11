export default function confetti(event, id) {
  


  /* 
  *
  * Modified and customized version of Szenia Zadvornykh’s work, “Party
  * Preloader,” on Codepen: https://codepen.io/zadvorsky/pen/CoDes
  * 
  */
  let Point = function(x, y) {
    this.x = x || 0;
    this.y = y || 0;
  };

  let Particle = function(ctx, p0, p1, p2, p3) {
    this.ctx = ctx;
    this.p0 = p0;
    this.p1 = p1;
    this.p2 = p2;
    this.p3 = p3;

    this.time = 0;
    this.duration = 2 + Math.random() * 1;
    // this.duration = 3 + 0.5;
    this.color =  '#' + Math.floor((Math.random() * 0xffffff)).toString(16);

    this.w = 8;
    this.h = 6;

    this.complete = false;
  };

  Particle.prototype = {
    update: function() {
      // (1/60) is timeStep
      this.time = Math.min(this.duration, this.time + (1/60));

      var f = Ease.outCubic(this.time, .0125, 1, this.duration);
      var p = cubeBezier(this.p0, this.p1, this.p2, this.p3, f);

      var dx = p.x - this.x;
      var dy = p.y - this.y;

      this.r =  Math.atan2(dy, dx) + (Math.PI * 0.5);
      this.sy = Math.sin(Math.PI * f * 10);
      this.x = p.x;
      this.y = p.y;

      this.complete = this.time === this.duration;
    },
    draw: function() {
      this.ctx.save();
      this.ctx.translate(this.x, this.y);
      this.ctx.rotate(this.r);
      this.ctx.scale(1, this.sy);

      this.ctx.fillStyle = this.color;
      this.ctx.fillRect(-this.w * 0.5, -this.h * 0.5, this.w, this.h);

      this.ctx.restore();
    }
  };

  function CelebrationCanvas(canvas, width, height) {
    var particles = [];
    var ctx = canvas.getContext('2d');

    canvas.width = width;
    canvas.height = height;
    createParticles();

    function animate() {
      requestAnimationFrame(loop);
    }

    function createParticles() {
      for (var i = 0; i < 128; i++) {
        var p0 = new Point(width * 0.5, height * 0.5);
        var p1 = new Point(Math.random() * width, Math.random() * height);
        var p2 = new Point(Math.random() * width, Math.random() * height);
        var p3 = new Point(Math.random() * width, height + 64);

        particles.push(new Particle(ctx, p0, p1, p2, p3));
      }
    }

    function update() {
      particles.forEach(function(p) {
        p.update();
      });
    }

    function draw() {
      ctx.clearRect(0, 0, width, height);
      particles.forEach(function(p) {
        p.draw();
      });
    }

    function loop() {
      update();
      draw();
      animate();
    }

    function checkParticlesComplete() {
      for (var i = 0; i < particles.length; i++) {
        if (particles[i].complete === false) return false;
      }
      return true;
    }

    return {
      animate: animate
    };
  }


  // var startButton = document.getElementById(idstart);
  // startButton.addEventListener('click', function(event) {
    var canvas = document.createElement('canvas');
    console.log(event);
    canvas.id = `confetti_${id}`
    canvas.width = 600;
    canvas.height = 600;
    canvas.style.position = 'absolute';
    canvas.style.left = (event.pageX - 100) + 'px'; // adjust if needed
    canvas.style.top = (event.pageY - 100) + 'px'; // adjust if needed
    document.body.appendChild(canvas);
    var celebrationCanvas = new CelebrationCanvas(canvas, 200, 200);
    celebrationCanvas.animate();
  // });



  // var celebrationCanvas = new CelebrationCanvas(document.getElementById('celebration'), 600, 600);

  // // celebrationCanvas.animate();

  // var startButton = document.getElementById('startAnimationButton');
  // startButton.addEventListener('click', function() {
  //   celebrationCanvas.animate();
  // });

  /**
   * easing equations from http://gizma.com/easing/
   * t = current time
   * b = start value
   * c = delta value
   * d = duration
   */
  var Ease = {
    inCubic: function (t, b, c, d) {
      t /= d;
      return c*t*t*t + b;
    },
    outCubic: function(t, b, c, d) {
      t /= d;
      t--;
      return c*(t*t*t + 1) + b;
    },
    inOutCubic: function(t, b, c, d) {
      t /= d/2;
      if (t < 1) return c/2*t*t*t + b;
      t -= 2;
      return c/2*(t*t*t + 2) + b;
    },
    inBack: function (t, b, c, d, s) {
      s = s || 1.70158;
      return c*(t/=d)*t*((s+1)*t - s) + b;
    }
  };

  function cubeBezier(p0, c0, c1, p1, t) {
    var p = new Point();
    var nt = (1 - t);

    p.x = nt * nt * nt * p0.x + 3 * nt * nt * t * c0.x + 3 * nt * t * t * c1.x + t * t * t * p1.x;
    p.y = nt * nt * nt * p0.y + 3 * nt * nt * t * c0.y + 3 * nt * t * t * c1.y + t * t * t * p1.y;

    return p;
  }



}