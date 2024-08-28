# password-manager

Password Manager CLI app. Store passwords locally in a secure way.

## What does it do?

Stores user's passwords in an encrypted local file or local database. The security is managed by a master password.

## How to use?

```bash
poetry run password_manager
```

This CLI app is interactive. No commands need to be passed here.
The master password is asked at the beginning.

## Commands

### Put

Stores a new password.

```bash
> put id password
```

#### Args

- id: String. Unique identifier of the password
- password: String. The password associated with this id

### Get

Returns the password based on the id.

```bash
> get id
```

#### Args

- id: String. Unique identifier of the password

### List

Returns list of all stored ids.

```bash
> list
```

### Delete

Deletes a password based on id.

```bash
> delete id
```

#### Args

- id: String. Unique identifier of the password

## Examples

```bash
# store a password
> put gmail abcdefgABCDEFG

# store another one
> put yahoo qwertyQWERTY

# get password of gmail
> get gmail
abcdefgABCDEFG

# list all passwords
> list
  gmail, yahoo

# delete yahoo
> delete yahoo

# list all passwords
> list
  gmail
```

## Installation

```bash
poetry install
poetry run password_manager
```
