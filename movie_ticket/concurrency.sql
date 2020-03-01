/* 
How to handle concurrency; such that no two users are able to book the same
seat? We can use transactions in SQL databases to avoid any clashes. For
example, if we are using SQL server we can utilize Transaction Isolation
Levels to lock the rows before we update them. Note: within a transaction,
if we read rows we get a write-lock on them so that they can’t be updated
by anyone else. Here is the sample code:
*/

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
 
BEGIN TRANSACTION;
 
    -- Suppose we intend to reserve three seats (IDs: 54, 55, 56)
    -- for ShowID=99 
    SELECT * FROM ShowSeat WHERE ShowID=99 && ShowSeatID IN (54, 55, 56) && isReserved=0 
 
    -- if the number of rows returned by the above statement is NOT three,
    -- we can return failure to the user.
    UPDATE ShowSeat TABLE...
    UPDATE Booking TABLE ...
 
COMMIT TRANSACTION;