/* eslint-disable max-classes-per-file */
/**
 * A class to provide template for objects that represent node of linked list.
 */
class LinkedListNode {
    /**
     * create a node of a linked list.
     * @param {Number} _value - value stored in the node.
     * @returns {LinkedListNode}
     * @memberof LinkedListNode
     */
    constructor(_value) {
        this.value = _value;
        this.next = null;
    }
}

/**
 * Class to provide template for objects that represent a linked list.
 */
class LinkedList {
    constructor() {
        this.head = null;
    }

    /**
     * adds a node to the linked list
     * @param {Number} value - number to be stored in a node.
     */
    add(value) {
        if (!this.head) {
            this.head = new LinkedListNode(value);
            return;
        }
        let currentNode = this.head;
        // eslint-disable-next-line no-constant-condition
        while (1) {
            if (currentNode.next) {
                currentNode = currentNode.next;
            } else {
                break;
            }
        }
        currentNode.next = new LinkedListNode(value);
    }

    /**
     * Reverses the linked list.
     */
    reverse() {
        let currentNode = this.head;
        let prevNode = null;
        while (currentNode.next) {
            if (currentNode === this.head) {
                prevNode = currentNode;
                currentNode = currentNode.next;
                prevNode.next = null;
            } else {
                const temp = currentNode.next;
                currentNode.next = prevNode;
                prevNode = currentNode;
                currentNode = temp;
            }
        }
        this.head = currentNode;
    }
}

const linkedList = new LinkedList();
for (let i = 0; i < 10; i += 1) {
    linkedList.add(i);
}
linkedList.reverse();
console.log(linkedList.head);
console.log('done');
