export default function remLike (id) {
    return fetch(`http://192.168.93.33:9001/api/remlike?id=${id}`, {method: 'POST'})
    .then(response => response.json())
    .then(response => {
        // console.log(response);
        return response;
    })
    .catch(err => {
        console.error(err);
        return err;
    });
}