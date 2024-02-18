export default function getPosts(offset = 0, limit = 10) {
    return fetch(`http://localhost:9001/api/posts?offset=${offset}&limit=${limit}`, {method: 'GET', headers: {'Origin': 'http://localhost:9001'}})
        .then(response => response.json())
        .then(response => {
            for (let i = 0; i < response.length; i++) {
                if (response[i].htmltext) {
                    response[i].htmltext = response[i].htmltext.replace(/\n/g, "<br>")
                    const regex = /<tg-emoji[^>]*>([^<]+)<\/tg-emoji>/g;
                    response[i].htmltext = response[i].htmltext.replace(regex, (match, emoji) => emoji);
                    response[i].htmltext = response[i].htmltext.length > 500 ? response[i].htmltext.slice(0, 500) + '<div style="color: #5383FF;">...<div>' : response[i].htmltext;
                    response[i].username = response[i].username.length > 12 ? response[i].username.substring(0, 12) + '...' : response[i].username;
                }
            }
            return response;
        })
        .catch(err => {
            console.error(err);
            return err;
        });
}