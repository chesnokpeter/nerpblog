<template>
    <div :class="['nav',{'fixed': fixed}]">
        <router-link  @click="bold('blog')" to="/" id="blog">nerps</router-link>
        <div class="sep">/</div>
        <router-link  @click="bold('prog')" to="/prog" id="prog">prog</router-link>
        <div class="sep">/</div>
        <router-link  @click="bold('about')"  to="/about" id="about">about</router-link>
    </div>
</template>

<script>
import { RouterLink } from 'vue-router'
export default {
    data() {
        return {
            idbold: '',
            fixed: false
        }
    },
    methods: {
        bold(id) {
            if ( this.idbold != id) {
                function addbold(id, weight) {
                    let element = document.getElementById(id);
                    if (element) {
                        element.style.fontWeight = weight;
                    }
                }
                addbold(this.idbold, '700')
                addbold(id, '1000')
                this.idbold = id
            }
        },
        initidbold() {
            let l = window.location.pathname.split('/')[1];
            if (l) {
                this.bold(l);
            } else {
                this.bold('blog');
            }
        }
    },
    mounted() {
        this.initidbold();
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

<style scoped lang="scss">
    .nav {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        gap: 10px;
        margin-top: -10px;
        margin-bottom: -10px;
        padding: 10px 0;

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
        color: #fff;
    }

    a:hover {
        color: #666;
        // background-color: black;
        /* box-shadow: 0px 0px 0px 10px #000; */
        // text-decoration: underline;
    }

</style>