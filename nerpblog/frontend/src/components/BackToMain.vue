<template>
    <div :class="['nav',{'fixed': fixed}]">
        <router-link to="/" id="back"> // back to main //</router-link>
    </div>
</template>


<script>
import { RouterLink } from 'vue-router'
export default {
    data() {
        return {
            fixed: false
        }
    },
    mounted() {
        window.addEventListener('scroll', async (event) => {
            if (window.scrollY > 150) {
                this.fixed = true
            } else if (window.scrollY < 150) {
                this.fixed = false
            }
        })
    }
}

</script>

<style scoped  lang="scss">
    .nav {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        gap: 10px;
        padding: 10px 0;
        margin: -10px 0;
        &.fixed {
            position: sticky;
            top: 0;
            background-color: #12121200;
            width: 100%;
            backdrop-filter: blur(10px);
        }
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
    color: #666;
        /* background-color: black; */
        /* box-shadow: 0px 0px 0px 10px #000; */
        /* text-decoration: underline; */
    }
</style>