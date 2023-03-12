<script>
import Contactpage from '../components/contactpage.svelte';
import Nouser from '../components/nouser.svelte';
let user;
const token = localStorage.getItem('token')
fetch('http://127.0.0.1:5000/api/me/user',{
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'Access-Control-Allow-Origin':'*'
        },
        body:JSON.stringify({'token':token})
})
.then(res => {return res.json()})
.then(response => {user = response.user.user})
</script>


{#if user}
    <Contactpage name={user}/>
{:else}
<Nouser/>
{/if}



