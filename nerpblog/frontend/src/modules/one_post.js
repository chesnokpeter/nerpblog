export default function getOnePost(id) {
    return fetch(`http://192.168.93.33:9001/api/post/${id}`, {method: 'GET'})
        .then(response => response.json())
        .then(response => {
            response.htmltext = response.htmltext.replace(/\n/g, "<br>")
            console.log(response);
            return response;
        })
        .catch(err => {
            console.error(err);
            return err;
        });
}