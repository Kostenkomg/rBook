package ru.ystu.rBook.service;

import ru.ystu.rBook.domain.Book;

import java.io.FileNotFoundException;

public interface BookService {
    Iterable<Book> getAll();

    Book get(Long id) throws FileNotFoundException;

    Book update(Long id, Book book);

    Book create(Book book);

    void delete(Long id);
}
