Django Migrations
=================

* This is a placeholder repository for understanding django migrations.

* Assume there are three branches `stage`, `dev1` and `dev2`.

* Code is being written in the latter two branches only.

* We can follow below workflow for consistent migrations:

    1. Migrations created in one branch (say, `dev1`) can be merged into `stage`.

    2. Developer working on `dev2` branch might have some migrations in her branch. But when she rebases `dev2` with `stage`, migrations applied in `dev1` get pulled in.

    3. `dev2` can run `python manage.py makemigrations`. If there are migration conflicts, django will compplain about it and suggest you to do `python manage.py makemigations --merge`. Do the same.
