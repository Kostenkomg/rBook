package ru.ystu.rBook.service;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import ru.ystu.rBook.domain.Book;
import ru.ystu.rBook.repository.BookRepository;

import java.io.FileNotFoundException;

@Service
@RequiredArgsConstructor
public class BookServiceImpl implements BookService {
    private final BookRepository repository;

    @Override
    public Iterable<Book> getAll() {
        return repository.findAll();
    }

    @Override
    public Book get(Long id) throws FileNotFoundException {
        return repository.findById(id).orElseThrow(FileNotFoundException::new);
    }

    @Override
    public Book update(Long id, Book book) {
        book.setId(id);
        return repository.save(book);
    }

    @Override
    public Book create(Book book) {
        return repository.save(book);
    }

    @Override
    public void delete(Long id) {
        repository.deleteById(id);
    }
}
