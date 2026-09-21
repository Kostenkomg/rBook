package ru.ystu.rBook.repository;

import org.springframework.data.repository.CrudRepository;
import ru.ystu.rBook.domain.Book;

public interface BookRepository extends CrudRepository<Book, Long> {
}
