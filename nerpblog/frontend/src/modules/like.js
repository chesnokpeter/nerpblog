export default function addLike (id) {
    return fetch(`http://localhost:9001/api/like?id=${id}`, {method: 'POST'})
    .then(response => response.json())
    .then(response => {
        return response;
    })
    .catch(err => {
        console.error(err);
        return err;
    });
}