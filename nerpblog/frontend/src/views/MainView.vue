<template>
    <nav-bar></nav-bar>
    <div class="sep">нерпы пишут блоги</div>
    <div class="list" id="list">
        <one-post v-for="i in posts" :title="i.title" :text="i.htmltext" :likes="i.likes" :author="i.username" :id="i.id" :media="i.media"></one-post>
    </div>
</template>


<script>
    import OnePost from '@/components/OnePost.vue'
    import getPosts from '@/modules/post.js'
    import NavBar from '@/components/NavBar.vue'

    export default {
        components: {
            OnePost, NavBar
        },
        data() {
            return {
                posts: []
            }
        },
        async mounted() {
            let a = await getPosts(); 
            this.posts = a
            window.addEventListener('scroll', async (event) => { 
                if (window.scrollY + window.innerHeight + 1 >= document.documentElement.scrollHeight) {
                    if (document.getElementById('list')) {
                        let countLoadedPosts = document.getElementById('list').childElementCount
                        if (countLoadedPosts > 0) {
                            let newPosts = await getPosts(countLoadedPosts);
                            console.log(newPosts);
                            for (let i = 0; i < newPosts.length; i++) {
                                this.posts.push(newPosts[i])
                            }
                        }                        
                    }
                }
            })
        }
    }


</script>

<style scoped>
    .list {
        display: flex;
        max-width: 400px;
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
        /* flex: 1 0 0; */
        /* align-self: stretch; */
    }
    .sep {
        color: #fff;
        font-family: 'Mulish';
        font-size: 16px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        text-decoration: none;
    }
</style>