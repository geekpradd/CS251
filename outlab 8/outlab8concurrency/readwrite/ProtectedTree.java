package readwrite;

import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.Condition;

public class ProtectedTree {
    final Lock lock = new ReentrantLock();
    final Condition allowedRead = lock.newCondition();
    private Tree tree;

    private int writeCount = 0;
    private int readCount = 0;
    public ProtectedTree(Tree cur){
        tree = cur;
    }
    public void write(int value){
        lock.lock();
        try {
            System.out.println("WE");
            this.tree.write(value);
            System.out.println("WX");
            writeCount++;
            if (writeCount > readCount){
                allowedRead.signal();
            }
        }
        finally {
            lock.unlock();
        }
    }
    public int read(int value) throws InterruptedException {
        lock.lock();
        int answer;
        try {
            while (readCount >= writeCount){
                allowedRead.await();
            }

            answer = this.tree.read(value);
            if (answer == value){
                System.out.println("RS");
                readCount++;
            }
            else {
                System.out.println("RF");
            }
        }
        finally {
            lock.unlock();
        }

        return answer;
    }
}