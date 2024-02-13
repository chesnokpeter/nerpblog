<template>
    <back-to-main></back-to-main>
    <div :class="['post',{'notLoaded': notLoaded}]">
        <div class="title">{{ post.title }}</div>
        <div class="menu">
            <button 
                id="likeBtn" 
                :class="['like',{'isClick': isClick, 'afterClick': afterClick}]" 
                v-bind:value="likeNum" @click="handleLikeBtn($event)"
            >
                {{ likeNum }}
                <img :src="`http://192.168.93.33:9001/icons/like/heart%20(${Math.floor(1 + Math.random() * (36 + 1 - 1))}).png`" alt="" height="20px" id="heartLike">
            </button>
            <div class="date">{{ post.date }}</div>
            <div class="nerpa"><div class="author">{{ post.username }}</div>
            </div>
        </div>
        <div v-html="post.htmltext"></div>
        <a class="opentg" :href="post.botlink">открыть в боте</a>
        <div class="comments">// комментов пока нету //</div>
    </div>
</template>


<script>
import BackToMain from '@/components/BackToMain.vue'
import getOnePost from '@/modules/one_post.js'
import addLike from '@/modules/like.js';
import remLike from '@/modules/remlike.js';
import confetti from '@/modules/confetti.js'

export default {
    components: {
        BackToMain
    }, 
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            post: {},
            isClick: false,
            afterClick: false,
            likeNum: 0,
            notLoaded: true
        }
    }, 
    async mounted() {
        this.post = await getOnePost(this.id)
        if (this.post) {
            this.notLoaded = false
            this.likeNum = this.post.likes
            if (localStorage.getItem("likeList")) {
                if (JSON.parse(localStorage.getItem('likeList')).includes(this.id)) {
                    this.isClick = false; 
                    this.afterClick = true;
                }
            }            
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
    }
}

</script>

<style scoped lang="scss">
    .comments {
        color: #666;
    }

    a {
        text-decoration: none;
    }
    .opentg {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        padding: 0px;
        align-self: stretch;
        margin: 10px 0px;
        background-color: #5383FF;
        color: #000;
        padding: 5px 0;
    }
    .opentg:hover {
        background: #000;
        color: #5383FF;
        text-decoration: underline;
    }

    .menu {
        display: flex;
        justify-content: space-between;
        width: 100%;
        align-items: center;
        gap: 10px;
    }

    .nerpa {
        display: flex;
    }

    .author {
        color: #5383FF;
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
        padding: 10px;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        border-radius: 20px;
        // background: #202020;
        color: #FFF;
        font-family: 'Mulish';
        font-size: 16px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        word-wrap:break-word;
        padding-top: 0;

        &.notLoaded {
            display: none;
        }
    }

    .post:hover {
        color: #FFF;
    }
</style>