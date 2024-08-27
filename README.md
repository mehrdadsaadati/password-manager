# password-manager

Password Manager CLI app. Store passwords locally in a secure way.

## What does it do?

Stores user's passwords in an encrypted local file or local database. The security is managed by a master password.

## How to use?

```bash
password_manager command arg --master master_key
```

For all the commands you can pass master key to unlock the vault. Otherwise master key is asked interactively.

## Commands

### Put

Stores a new password.

```bash
password_manager put id password
```

#### Args

- id: String. Unique identifier of the password
- password: String. The password associated with this id

### Get

Returns the password based on the id.

```bash
password_manager get id
```

#### Args

- id: String. Unique identifier of the password

### List

Returns list of all stored ids.

```bash
password_manager list
```

### Delete

Deletes a password based on id.

```bash
password_manager delete id
```

#### Args

- id: String. Unique identifier of the password

## Examples

```bash
# store a password
password_manager put gmail abcdefgABCDEFG

# store another one
password_manager put yahoo qwertyQWERTY

# get password of gmail
password_manager get gmail
> abcdefgABCDEFG

# list all passwords
password_manager list
> gmail
> yahoo

# delete yahoo
password_manager delete yahoo

# list all passwords
password_manager list
> gmail
```

## Installation

```bash
poetry install
poetry run password_manager
```
