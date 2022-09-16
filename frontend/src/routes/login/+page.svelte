<script>
    export let data;
    export let form;
</script>


{#if form?.success}
    <p>Successfully logged in! Welcome back, <b>{form.login}</b></p>
{/if}

<div>
    <h1>LogIn Form</h1>
    <a href="/">Home</a>

    <form method="POST" action="/login">
        <input name="username" type="text">
        <input name="password" type="password">
        <button>Log in</button>
    </form>
</div>
