<template >
    <div class="comment">
        <div class="title">
            нерпа_<div class="username">{{ username }}</div>  {{ date }} //
        </div>
        <div class="body">{{ text }}</div>
    </div>
</template>

<script>

export default {
    props: {
        text: {
            type: String,
            required: true
        },
        username: {
            type: String,
            required: true
        },
        date: {
            type: String,
            required: true
        },
    }
}
</script>

<style scoped>
    .title {
        display: flex;
        color: #666666;
    }

    .username {
        color: #5383FF;
    }

    .comment {
        display: flex;
        flex-direction: column;
        font-size: 14px;
        background-color: #202020;
        justify-content: center;
        color: #fff;
        padding: 5px;
        padding-left: 10px;
        gap: 2px;
        border-radius: 10px;
    }
</style>