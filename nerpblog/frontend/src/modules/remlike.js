export default function remLike (id) {
    return fetch(`/api/remlike?id=${id}`, {method: 'POST'})
    .then(response => response.json())
    .then(response => {
        return response;
    })
    .catch(err => {
        console.error(err);
        return err;
    });
}