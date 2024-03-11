<template>
    <back-to-main></back-to-main>
    <div :class="['post',{'notLoaded': notLoaded}]">
        <p class="title">{{ post.title }}</p>
        <p class="htmltext" v-html="post.htmltext"></p>
        <div class="media" v-if="post.media">
            <div v-for="i in post.media">
                <img :src="`/media/photo/${i}`" alt="" class="img"  style="max-width: 300px;">
            </div>
        </div>
        <div class="menu">
            <button 
                id="likeBtn" 
                :class="['like',{'liked':liked}]" 
                v-bind:value="likeNum" @click="handleLikeBtn($event)"
            >
                {{ likeNum }}
                <img :src="`/icons/like/heart%20(${Math.floor(1 + Math.random() * (36 + 1 - 1))}).png`" alt="" height="20px" id="heartLike">
            </button>
            <div class="date">{{ post.date }}</div>
            <div class="nerpa">нерпа_<div class="author">{{ post.username }}</div>
            </div>
        </div>    
        <div @click="commExpand()" :class="['comments',{'expanded': commExpanded}]">
            комментарии {{ comments.length }}
            <img class="arrowDown" :src="`/icons/ui/arrowdown.svg`" alt="">
        </div>
        <div class="commentShow" v-if="commentShow">
            <div class="commentShowText">чтобы оставить комментарий, откройте статью в боте</div>
            <one-comment v-for="i in comments" :text="i.text" :date="i.date" :username="i.username"></one-comment>
        </div>    
    </div>       
    <div class="empty" style="margin-bottom: 30px;"></div>
    <!-- <by-chesnok :class="['by',{'notLoaded': notLoaded}]" style="margin-bottom: 50px;"></by-chesnok> -->
    <a :class="['opentg',{'notLoaded': notLoaded}]" :href="post.botlink">открыть в боте <img class="arrow-expand" :src="`/icons/ui/arrowexpand.svg`" alt=""></a>

</template>


<script>
import BackToMain from '@/components/BackToMain.vue'
import getOnePost from '@/modules/one_post.js'
import addLike from '@/modules/like.js';
import remLike from '@/modules/remlike.js';
import confetti from '@/modules/confetti.js'
import ByChesnok from '@/components/ByChesnok.vue'
import OneComment from '@/components/OneComment.vue'
import get_comment from '@/modules/get_comment.js'

export default {
    components: {
        BackToMain, ByChesnok, OneComment
    }, 
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            comments: [{}, {}, {}, {}], //! ВРЕМЕННО,
            commExpanded: false,
            post: {},
            likeNum: 0,
            notLoaded: true,
            liked: false,
            commentShow: false
        }
    }, 
    async mounted() {
        this.post = await getOnePost(this.id)
        this.comments = await get_comment(this.id)
        if (this.post) {
            this.notLoaded = false
            this.likeNum = this.post.likes
            if (localStorage.getItem("likeList")) {
                if (JSON.parse(localStorage.getItem('likeList')).includes(this.id)) {
                    // this.isClick = false; 
                    // this.afterClick = true;
                    this.liked = true
                }
            }            
        }

    },
    methods: {
        async handleLikeBtn(event) {
            if (localStorage.getItem("likeList")) {
                if (JSON.parse(localStorage.getItem('likeList')).includes(this.id)) {
                    // if (this.afterClick) {
                        let LikeList = JSON.parse(localStorage.getItem("likeList"))
                        let remLikeList = LikeList.filter((LikeList) => LikeList !== this.id)
                        localStorage.setItem('likeList', JSON.stringify(remLikeList))
                        this.likeNum -= 1
                        this.liked = false
                        await remLike(this.id)
                    // }
                } else {
                    await this.handleLike(event)
                }
            } else {
                await this.handleLike(event)
            }
        },
        async handleLike(event) {
            this.likeNum += 1
            this.liked = true
            let LikeList = JSON.parse(localStorage.getItem("likeList"))
            if (!LikeList) {LikeList = []}
            LikeList.push(this.id)
            localStorage.setItem('likeList', JSON.stringify(LikeList))
            confetti(event, this.id)
            await addLike(this.id)
            setTimeout(() => { 
                let confetti = document.getElementById(`confetti_${this.id}`)
                if (confetti) {
                    confetti.remove()
                }
            }, 2000);
        },
        commExpand() {
            if (this.commExpanded) {
                this.commExpanded = !this.commExpanded
            } else if (!this.commExpanded) {
                this.commExpanded = !this.commExpanded
            } 
            this.commentShow = !this.commentShow
        }
    }
}

</script>

<style scoped lang="scss">
    .htmltext {
        @media (max-width: 400px) {
            padding: 0 5px;
        }
    }
    .commentShowText {
        margin-bottom: 5px;
        display: flex;
        justify-content: center;
        width: 100%;
    }
    .commentShow {
        font-family: 'Mulish';
        font-size: 12px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        color: #666666;
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 5px;
        transition: 1s;
    }
    .comments {
        background-color: #202020;
        height: 30px;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
        gap: 5px;
        color: #666;
        &.expanded {
            .arrowDown {
                transform: rotate(180deg);
            }
        }
    }
    .arrowDown {
        transition: 0.2s;
    }
    .by {
        display: flex;
        &.notLoaded {
            display: none;
        }
    }
    .date {
        color: #666;
        font-size: 14px;
    }
    p {
        margin: 0;
    }
    .img {
        max-width: 400px;
        max-height: 400px;
    }
    a {
        text-decoration: none;
        margin: 0;
    }
    .opentg {
        display: flex;
        gap: 10px;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        padding: 0px;
        align-self: stretch;
        // margin: 10px 0px;
        background-color: #5383FF;
        color: #000;
        padding: 5px 0;
        font-family: 'Mulish';
        font-size: 16px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        position: fixed;
        width: 100vw;
        bottom: 0;
        &.notLoaded {
            display: none;
        }
    }
    .opentg:hover {
        background: #000;
        color: #5383FF;
        // text-decoration: underline;
    }
    .opentg:hover .arrow-expand {
        background: #5383FF;
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
        color: #666;
        font-size: 14px;
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
        &.liked {
            color: #000;
            border: #5383FF solid 2px;
            box-shadow: none;
            background-color: #5383FF;
        }
    }
    .like:hover {
        border: #5383FF solid 2px;
    }
    .post {
        display: flex;
        max-width: 400px;
        width: 100%;

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
        &.notLoaded {
            display: none;
        }

        @media (max-width: 420px) {
            // padding: 0 10px;
        }
    }

</style>