import os
import textwrap


def generate_env_file():
    env_content = textwrap.dedent(f"""
        # DB Settings
        DB_ENGINE=postgresql+asyncpg
        DB_USER=postgres
        DB_PASSWORD=12345
        DB_HOST=localhost
        DB_NAME=db_name
        DB_PORT=5432

        # Image directory
        PATH_TO_IMAGE_DIRECTORY=app\\media

        # Root directory
        ROOT_DIR={os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}
                                  """)

    with open('../../.env', 'w') as env_file:
        env_file.write(env_content.strip())

    print('.env file generated successfully.')


if __name__ == '__main__':
    generate_env_file()
