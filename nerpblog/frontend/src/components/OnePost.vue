<template>
    <div class="post">
        <router-link :to="{ name: 'post', params: { id: id }}" class="title">{{ title }}</router-link>
        <div v-html="text"></div>
        <div class="bott">
            <button 
                id="likeBtn" 
                :class="['like',{'isClick': isClick, 'afterClick': afterClick}]" 
                v-bind:value="likeNum" @click="handleLikeBtn($event)"
            >
                {{ likeNum }}
                <img :src="`http://192.168.93.33:9001/icons/like/heart%20(${Math.floor(1 + Math.random() * (36 + 1 - 1))}).png`" alt="" height="20px" id="heartLike">
            </button>
                <div class="nerpa"><div class="author">{{ author }}</div>
            </div>
        </div>
    </div>
</template>

<script>
    import addLike from '@/modules/like.js';
    import remLike from '@/modules/remlike.js';
    import confetti from '@/modules/confetti.js'
    import { RouterLink } from 'vue-router'

export default {
    props: {
        text: {
            type: String,
            required: true
        },
        title: {
            type: String,
            required: true
        },
        likes: {
            type: Number,
            required: true
        },
        author: {
            type: String,
            required: true
        },
        id: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            likeNum: this.likes,
            isClick: false,
            afterClick: false
        }
    },
    methods: {
        async handleLikeBtn(event) {
            if (localStorage.getItem("likeList")) {
                if (JSON.parse(localStorage.getItem('likeList')).includes(this.id)) {
                    if (this.afterClick) {
                        let LikeList = JSON.parse(localStorage.getItem("likeList"))
                        let remLikeList = LikeList.filter((LikeList) => LikeList !== this.id)
                        localStorage.setItem('likeList', JSON.stringify(remLikeList))
                        this.likeNum -= 1
                        this.isClick = false; 
                        this.afterClick = false;
                        await remLike(this.id)
                    }
                } else {
                    await this.handleLike(event)
                }
            } else {
                await this.handleLike(event)
            }
        },
        async handleLike(event) {
            this.likeNum += 1
            this.isClick = true
            let LikeList = JSON.parse(localStorage.getItem("likeList"))
            if (!LikeList) {LikeList = []}
            LikeList.push(this.id)
            localStorage.setItem('likeList', JSON.stringify(LikeList))
            confetti(event, this.id)
            await addLike(this.id)
            setTimeout(() => { this.isClick = false; this.afterClick = true;
                let confetti = document.getElementById(`confetti_${this.id}`)
                if (confetti) {
                    confetti.remove()
                }
            }, 2000);
        }
    },
    mounted() {
        if (localStorage.getItem("likeList")) {
            if (JSON.parse(localStorage.getItem('likeList')).includes(this.id)) {
                this.isClick = false; 
                this.afterClick = true;
            }
        }
    }
}
</script>

<style scoped lang="scss">

    .title:hover {
        text-decoration: underline;
        background-color: #000;
    }

    .bott {
        display: flex;
        justify-content: space-between;
        width: 100%;
        align-items: center;
    }

    .nerpa {
        display: flex;
    }

    a {
        text-decoration: none;
        color: #FFF;
    }

    .author {
        color: #5383FF;
        padding-left: 20px;
    }

    .like {
        height: 30px;
        display: flex;
        padding: 10px 10px;
        align-items: center;
        gap: 10px;
        background-color: #202020;
        font-family: 'Mulish';
        font-size: 14px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        border: none;
        color: #FFF;
        border: #FFF solid 2px;
        border-radius: 16px;
        transition: 0.2s ease-out;
        justify-content: center;
        align-items: center;
        &.isClick {
            color: #000;
            border: #5383FF solid 2px;
            box-shadow: 0px 0px 10px 1px #5383FF;
            background-color: #5383FF;
            // transform: scale(1.2)
        }
        &.afterClick {
            color: #000;
            border: #5383FF solid 2px;
            box-shadow: none;
            background-color: #5383FF;
            // transform: scale(1.2)
        }
    }

    .like:hover {
        border: #5383FF solid 2px;
    }

    .post {
        display: flex;
        max-width: 400px;
        padding: 12px;
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
        border-radius: 20px;
        background: #202020;
        color: #FFF;
        font-family: 'Mulish';
        font-size: 16px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        word-wrap:break-word;
    }

    .post:hover {
        color: #FFF;
    }
</style>