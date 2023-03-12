<script>
import Home from "./routes/Home.svelte";
import Me from "./routes/me.svelte";
import Fogort from "./routes/fogort.svelte";
import Notfound from "./routes/Notfound.svelte";
import Router from 'svelte-spa-router';
import Signup from './routes/signup.svelte';
</script>

<Router routes={{
	'/':Home,
	'/me':Me,
	'/fogort':Fogort,
	'/signup':Signup,
	'*':Notfound,

}}/>


