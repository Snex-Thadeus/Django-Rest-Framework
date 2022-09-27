const loginForm = document.getElementById('login-form')
const baseEndpoint = "http://localhost:8000/api"

if (loginForm) {
    // handle this form
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event) {
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm) // it does not matter what the ids are on the form
    let loginObjectData = Object.fromEntries(loginFormData)
    console.log(loginObjectData)

    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(loginObjectData)
    }
    fetch(loginEndpoint, options) // Asynchronous Promise
    .then(response=>{
        console.log(response)
        return response.json()
    })
    .then(x => {
        console.log(x)
    })
}