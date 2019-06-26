template <class Key, class Value, class KeyOfValue, class Compare, class Alloc>
typename rb_tree<Key, Value, KeyOfValue, Compare, Alloc>::iterator // 返回值
rb_tree<Key, Value, KeyOfValue, Compare, Alloc>::__insert(base_ptr x_, base_ptr y_, const Value& v){
    link_type x = (link_type) x_;
    link_type y = (link_type) y_;
    link_type z;

    if (x != 0 || y == header || key_compare(KeyOfValue()(v), key(y))){
        // v 比 y 小，插入到左边
        z = create_node(v);
        left(y) = z; // 当y为header,则有leftmost() = z;
        if (y == header){
            root() = z; // header->parent
            rightmost() = z;
        } else if (y == leftmost()){
            leftmost() = z;
        }
    } else {
        z = create_node(v);
        right(y) = z;
        if (y == header){
            root() = z;
            leftmost() = z;
        } else if (y == rightmost()){
            rightmost() = z;
        }
    }
    parent(z) = y;
    left(z) = 0;
    right(z) = 0;

    __rb_tree_rebalance(z, header->parent);
    ++node_count;
    return iterator(z);
}