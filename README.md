# ReIdeas - An Idea Reminder

This is an open source script that helps you remember your forgotten ideas on Twitter. The script uses the Fibonacci Sequence forgetting curve to remind you of your past content at the perfect time, making it easy to revive old ideas or come up with new ones.

## Reminder Email

![image](https://user-images.githubusercontent.com/25631641/227734357-fc03fec3-021b-4529-ab9f-483fa9a62638.png)

## TODO
```

          +--------+             +-----------------+
          | Twitter|             | Other Platforms |
          +--------+             +-----------------+
                |                       |
                +-----------+-----------+
                            |
                      +-----------+
                      |   ReIdea  |
                      +-----------+
                            |
                +-----------+-----------+
                |                       |
          +--------+              +--------+
          | User1  |              | User2  |
          +--------+              +--------+
```
## Usage

To use the script, you'll need to set up a GitHub Actions workflow that runs the script on a daily basis. Here's how to do it:

1. Use this template this repository to your own account.
2. **Set up the required secrets in your repository's settings:**
   - `PASSWORD`: Your Gmail password or app password.
   - `FROM_EMAIL`: Your Gmail email address.
   - `TO_EMAIL`: The recipient's email address for the reminder.
   - `USERNAME`: Your Twitter username.

![image](https://user-images.githubusercontent.com/25631641/227734091-dc774ec3-1b8b-42f8-aa40-2739592b9823.png)

3. It will update the variables in the the `.github/workflows/reminder.yml` file with the correct secrets and schedule:
   - `PASSWORD`: `${{ secrets.PASSWORD }}`
   - `FROM_EMAIL`: `${{ secrets.FROM_EMAIL }}`
   - `TO_EMAIL`: `${{ secrets.TO_EMAIL }}`
   - `USERNAME`: `${{ secrets.USERNAME }}`
   - `schedule`: The cron expression that specifies when the workflow should run. The default is set to run every day at midnight UTC (`"0 0 * * *"`).
4. The script will now run on a daily basis and send you a reminder email of your old tweets at the perfect time.

## Security

This script requires the use of sensitive information, such as your Gmail password or app password, and your email addresses. To keep this information secure, we recommend that you store them as GitHub secrets. This ensures that the secrets are encrypted and not publicly visible in your code or repository.

To set up secrets in your repository, go to your repository's **Settings** > **Secrets** and add the required secrets. Then reference them in your workflow file using `${{ secrets.SECRET_NAME }}` syntax.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
