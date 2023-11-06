
const apiHost = 'http://127.0.0.1:8000/api/'

export default class PostService {
    static async getAll(filter = 'created_at') {
        try {
            const response = await fetch(`${apiHost}news/statistics?filter=${filter}`);
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error in PostService.getAll:', error);
            throw error;
        }
    }
}