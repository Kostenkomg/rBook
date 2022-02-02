package ru.ystu.rBook.domain;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Entity
@Table(name = "book")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Book {
    @Id
    @GeneratedValue
    private Long id;
    @Column
    private String title;
    @Column
    private String year;
    @Column
    private String authors;
    @Column
    private String genres;

}
