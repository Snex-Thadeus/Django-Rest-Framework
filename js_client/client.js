const contentContainer = document.getElementById('content-container')
const loginForm = document.getElementById('login-form')
const searchForm = document.getElementById('search-form')
const baseEndpoint = "http://localhost:8000/api"

if (loginForm) {
    // handle this form
    loginForm.addEventListener('submit', handleLogin)
}

if (searchForm) {
    // handle this form
    searchForm.addEventListener('submit', handleSearch)
}


function handleLogin(event) {
    // console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm) // it does not matter what the ids are on the form
    let loginObjectData = Object.fromEntries(loginFormData)
    // console.log(loginObjectData)

    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(loginObjectData)
    }
    fetch(loginEndpoint, options) // Asynchronous Promise
    .then(response=>{
        // console.log(response)
        return response.json()
    })
    .then(authData => {
        handleAuthData(authData, getProductList)
    })
}

function handleSearch(event) {
    event.preventDefault()

    let formData = new FormData(searchForm)
    let data = Object.fromEntries(formData)
    let searchParams = new URLSearchParams(data)

    const endpoint = `${baseEndpoint}/search/?${searchParams}`
    const headers = {
        "Content-Type": "application/json",
    }
    const authToken = localStorage.getItem('access')
    if (authToken){
        headers['Authorization'] = `Bearer ${authToken}`
    }

    const options = {
        method: "GET",
        headers: headers
    }
    fetch(endpoint, options) 
    .then(response=>{
        return response.json()
    })
    .then(data => {
        writeToContainer(data)
    })
}



function handleAuthData(authData, callback) {
    localStorage.setItem('access', authData.access)

    localStorage.setItem('refresh', authData.refresh)

    if (callback) {
        callback()
    }
} 

function writeToContainer(data){
    if (contentContainer) {
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

function getFetchOptions(method, body){
    const options = {
        method: method == null ? "GET" : method,
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('access')}`

        },
        body: body ? body : null
    }
}

function isTokenNotValid(jsonData){
    if (jsonData.code && jsonData.code === "token_not_valid") {
        alert("Please Login Again!")
        return false
    }
    return true
}


function validateJWTToken(){
    // fetch
    const endpoint = `${baseEndpoint}/token/verify/`
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"

        },
        body: JSON.stringify({token: localStorage.getItem('access')})
    }
    fetch(endpoint, options) 
    .then(response=> response.json())
    .then(x=> {
        console.log(x)
        isTokenNotValid(x)
    })
}


function getProductList(){
    const endpoint = `${baseEndpoint}/product/`
    const options = getFetchOptions()
    fetch(endpoint, options)
    .then(response=>{
        
        return response.json()

    })
    .then(data=> {
        const validData = isTokenNotValid(data)
        if (validData) {
            writeToContainer(data)
        }
        
    })
    
}
// getProductList()
validateJWTToken()