<template>
    <div id="home">
        <div>
            <span class="explain">Faker is </span>
            <span class="start">start</span>
        </div>
        <div class="example">sample movie</div>
        <div id="sample" v-on:scroll="makeScroll">
            <div class="box"><h3>1</h3></div>
            <div class="box"><h3>2</h3></div>
            <div class="box"><h3>3</h3></div>
            <div class="box">4</div>
            <div class="box">5</div>
            <div class="box">6</div>
            <div class="box">7</div>
            <div class="box">8</div>
            <div class="box">9</div>
            <div class="box">10</div>
        </div>
    </div>
</template>

<script>
export default {
  methods: {
    makeScroll: function () {
      let diff = 0
      let ticking = false
      // const wheelEvent = 'onwheel' in document.createElement('div') ? 'wheel' : 'mousewheel'
      const list = document.getElementById('sample')
      //   const list = document.querySelector('ul')

      function doSomething (diff) {
        list.scrollLeft += (diff) * 0.3
      }

      list.addEventListener('wheel', function (e) {
        diff = e.deltaY
        if (!ticking) {
          window.requestAnimationFrame(function () {
            doSomething(diff)
            ticking = false
          })
        }
        ticking = true
      }, { passive: true })
    }
  }
}
</script>

<style>
#home{

}
#sample {
    display: flex;
    padding: 0;
    display: block;
    white-space: nowrap;
    height: 100%;
    overflow-y: visible;
    overflow-x: scroll;
    padding: 0;
    font-size: 0;
    padding-top:100px;
    padding-bottom: 100px;
    /* align-items: center;
    justify-content: center; */
}
#sample .box{
    width: 300px;
    height: 400px;
    box-sizing: border-box;
    display: inline-block;
    margin-right: 5px;
    border: 2px solid white ;
    color : white;
}
#sample .box:hover{
    border:2px solid #ffb917;
    background: black;
    overflow-y: visible;
    transform: scale( 1.1 );
    color : white;
}
</style>
