export default function getPosts(offset = 0, limit = 10) {
    return fetch(`http://192.168.93.33:9001/api/posts?offset=${offset}&limit=${limit}`, {method: 'GET', headers: {'Origin': 'http://192.168.93.33:9001'}})
        .then(response => response.json())
        .then(response => {
            // response.htmltext = response.htmltext.replace(/\n/g, "<br>")
            for (let i = 0; i < response.length; i++) {
                response[i].htmltext = response[i].htmltext.replace(/\n/g, "<br>")
                
            }
            console.log(response);
            return response;
        })
        .catch(err => {
            console.error(err);
            return err;
        });
}