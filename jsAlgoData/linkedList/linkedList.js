class Node {
    constructor(element){
        this.element = element
        this.next = null
    }

}

class myLinkedList{
    constructor(){
        this.head = new Node('head')
    }
    
    findByValue(target){
        let cur = this.head.next
        while(cur !== null && cur.element!== target){
            cur = cur.next
        }

        return cur === null ? -1 : cur
    }
    findByIndex(target){
        let index = 0
        let cur = this.head.next
        while(cur !== null && index !== target){
            cur = cur.next
            index += 1
        }

        return cur === null ? -1 : index
    }

    append(newElement){
        const newNode = new Node(newElement)
        let cur = this.head
        while(cur.next){
            cur = cur.next
        }
        cur.next = newNode
    }

    insertAfter(newElement,element){
        const cur = this.findByValue(element)
        if(cur == -1){
            console.log(`no node of value ${element} found`)
            return
        }
        const newNode = new Node(newElement)
        currentNode.next = newNode
    }

    findPrev(target){
        let cur = this.head
        while(cur.next!==null && cur.element !== target){
            cur = cur.next
        }
        if(cur.next === null ){
            return -1
        }
        return cur
    }

    remove(target){
        const pre = this.findPrev(target)
        if(pre === -1){
            console.log(`none is find`)
            return
        }
        pre.next = pre.next.next
    }
    // head -> Node1 -> Node2 -> Node3 -> Node4
    // O(n) time & O(1) space
    reverse(){
        let tmp,pre
        let cur = this.head.next
        while(cur !== null){
            //save next before we over writer
            tmp = cur.next 
            cur.next  = pre
            // reverse pointer
            pre = cur
            cur = tmp
        }
        this.head.next = pre

        //     // O(n) time & O(n) space
        // function reverse(head) {
        //     if (!head || !head.next) {
        //       return head;
        //     }
        //     let tmp = reverse(head.next);
        //     head.next.next = head;
        //     head.next = undefined;
        //     return tmp;
        //   }
    }



    dispaly(){
        let current = this.head.next
        let container = []
        while(current !== null ){
            container.push(current.element)
        }
        console.log(container.join(' -> '))
    }

}


// test

function test() {
    const list = new myLinkedList()
    for(let i = 1; i<5; i++){
        list.append(i)
    }
    list.dispaly()
    // list.reverse()
    // list.dispaly()
}
test()

