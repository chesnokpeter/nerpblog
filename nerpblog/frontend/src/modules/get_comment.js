export default function get_comment (id) {
    return fetch(`/api/post/${id}/comments`, {method: 'GET'})
    .then(response => response.json())
    .then(response => {
        for (let i = 0; i < response.length; i++) {
            if (response[i].text) {
                response[i].date = new Date(response[i].date); 
                let formattedDate = response[i].date.toLocaleTimeString('ru-RU', {hour: '2-digit', minute: '2-digit'}); 
                let outputString = `${formattedDate}D${response[i].date.getDate() < 10 ? '0' : ''}${response[i].date.getDate()}.${response[i].date.getMonth() + 1 < 10 ? '0' : ''}${response[i].date.getMonth() + 1}`;
                response[i].date = outputString;
            }
        }
        return response;
    })
    .catch(err => {
        console.error(err);
        return err;
    });
}