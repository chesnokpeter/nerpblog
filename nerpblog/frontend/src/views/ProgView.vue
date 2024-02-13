<template>
    <nav-bar></nav-bar>
    <div class="text">
        open-source full stack SPA <br>
        fastapi vue vite aiogram <br>
        sqlalchemy postgresql <br>
        <a href="https://github.com/chesnokpeter/nerpblog">github.com/chesnokpeter/nerpblog</a> 
        <a href="https://t.me/nrpblgbot">@nrpblgbot</a>
    </div>
    <div class="text">поддержка сайта осуществляется исключительно за счёт автора<by-chesnok></by-chesnok></div>
</template>


<script>
import NavBar from '@/components/NavBar.vue'
import ByChesnok from '@/components/ByChesnok.vue'

export default {
    components: {
        NavBar, ByChesnok
    }
}

</script>

<style scoped>
    .text {
        color: #FFF;
        font-family: 'Mulish';
        font-size: 16px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        display: flex;
        text-align: center;
        word-wrap: break-word;
        flex-direction: column;
        align-items: center;
    }
    a {
        color: #5383FF;
        text-decoration: none;
    }
</style>