# single-thread, in-memory database

Data Commands
* SET
* GET
* DELETE
* COUNT

Transaction commands
BEGIN
ROLLBACK
COMMIT

1) Get data commands to work on its own first
 * Keep a dictionary for database, as well as for count of values
   * Ex) SET A 10 -> data['A'] = 10
     * GET: O(1)
     * SET: O(1)
     * DELETE: O(1)
     * COUNT:
       * this returns the number of variables equal to [value]
       * another dict necessary
 * Get it to work from string input rather than function call, to make transaction easier

2) Transaction commands
 * BEGIN
   * implies a stack to be used
   * Create a stack of commands, executing only when COMMIT is received
   * use stack of stack
 * ROLLBACK
   * go back to previous commit
   * clear stack of commands
 * COMMIT
   * execute

orig_copy[
BEGIN
  set a 10 
  BEGIN
    set b 10
    BEGIN
      set c 10
      get a
        new_data=orig_copy
