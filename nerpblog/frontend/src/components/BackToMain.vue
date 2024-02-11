<template>
    <div class="nav">
        <router-link to="/" id="back"> // back to main //</router-link>
    </div>
</template>


<script>
import { RouterLink } from 'vue-router'
export default {

}

</script>

<style scoped>
    .nav {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        gap: 10px;
    }

    a, .sep {
    color: #FFF;
    font-family: 'Mulish';
    font-size: 16px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    text-decoration: none;
}

a:hover {
        background-color: black;
        /* box-shadow: 0px 0px 0px 10px #000; */
        text-decoration: underline;
    }
</style>