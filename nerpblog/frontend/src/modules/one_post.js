export default function getOnePost(id) {
    return fetch(`http://localhost:9001/api/post/${id}`, {method: 'GET'})
        .then(response => response.json())
        .then(response => {
            if (response.htmltext) {
                response.username = response.username.length > 12 ? response.username.substring(0, 12) + '...' : response.username;
                response.htmltext = response.htmltext.replace(/\n/g, "<br>")
                response.date = new Date(response.date); 
                let formattedDate = response.date.toLocaleTimeString('ru-RU', {hour: '2-digit', minute: '2-digit'}); 
                let outputString = `${formattedDate}D${response.date.getDate() < 10 ? '0' : ''}${response.date.getDate()}.${response.date.getMonth() + 1 < 10 ? '0' : ''}${response.date.getMonth() + 1}`;
                response.date = outputString;
                return response;                
            }
            return false
        })
        .catch(err => {
            console.error(err);
            return false;
        });
}