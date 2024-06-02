# PyEasyMailer

PyEasyMailer is a command line tool to send email templates from a linux server using a remote SMTP such as Zoho or GMail. 

## Installation

- Clone the installation script using git
  - ``` git clone https://gist.github.com/lilrebel17/d81bd3f01e62c91c05cbcf720b9fcbda```
- Navigate into the newly downloaded directory
  - Run ```./install.sh```


## Setup

Once PyEasyMailer is installed, use the following command to run the interactive setup:

```bash
pyeasymailer setup
```

## Usage Examples
```bash
# Runs interactive setup to setup SMTP credentials and server information
pyeasymailer setup

# Creates a template with the name, subject & body provided.
pyeasymailer template -c -n [template_name] -s [template_subject] -b [template_body] 

#Sends template email with the name provided.
pyeasymailer send -n [template_name] 
```


#### Setup Subcommand
- Runs interactive setup to setup SMTP credentials and server information.
- ```bash
    pyeasymailer setup
    ``` 

#### Template Subcommand
- Allows you to create & modify templates.
- Example
  - ```bash
    # This would create a new template with the name "Hello".
    # The body would just say "Hello!"
    # The subject would be "A hello from me"
    # It attach a file with the name test.txt to your email with the contents of /home/you/test.txt
    pyeasymailer template -c -n Hello -b "Hello!" -s "A hello from me" -a '/home/you/test.txt'
    ```
- Arguments
  - Required Flags (Must have at least one)
    - -m or --modify to modify a template
    - -c or --create to create a new template
    - -l or --list to list all created template names
  - Optional Arguments (Only required if -m or -c is provided)
    - -b or --body to set the body of a template
    - -s or --subject to set the subject of a template
    - -n or --name to set the name of a template.
    - -a or --attachment to set the filepath to an attachment you want to send

#### Send Subcommand
- Allows you to send one of your templates to a specified email address
- Example
  - ```bash
    # This would send the "Hello" template to example@email.com
    pyeasymailer send -n Hello -t example@email.com
    ```
- Arguments
  - -n or --name to pick the template you want to choose
  - -t or -to to set the email address you want to send the email to.

## Contributing

Contributions are welcome! If you'd like to contribute to PyEasyMailer, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

PyEasyMailer is released under the [GNU General Public License v3.0](LICENSE).

## Contact

For questions or support, please open an issue [here](https://github.com/lilrebel17/pyeasymailer/issues)
