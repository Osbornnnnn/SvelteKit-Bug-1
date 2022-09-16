export const actions = {
	default: async ({request}) => {
        const data = await request.formData();
        const username = data.get('username');
        const password = data.get('password');
        const res = await fetch("http://localhost:8000/signin", {method: "POST", body: data});
        console.log(data)
        return { success: true, username: username};
    }
};
